macro "convert ca timeseries czi"{

	//folder selection cwith input files
	loadfolder = getDirectory("Choose Directory where czi files are located.");

	//parameter selection
	Dialog.create("convert czi timeseries to single tiffs");
  	Dialog.addNumber("number of timeseries cycles of live marker (2 channels, e.g. 1:Ca++ and 2:brightfield):", 3);
    Dialog.addNumber("number of frames per timeseries cycle of live marker (2 channels, e.g. 1:Ca++ and 2:brightfield):", 76);
    Dialog.addNumber("number of frames of final timeseries (3 channels, e.g. 1:Ca++, 2:asc, 3:brightfield ):", 16);
    Dialog.show();
    nr_ca_cycles = Dialog.getNumber();
    nr_frames_ca = Dialog.getNumber();
    nr_frames_specking = Dialog.getNumber();


	
	
	//detect czi files to convert
	reg = ".*\.czi"; // regex to filter filesnames with ending czi	
	filenames = getFilteredFileList(loadfolder, reg);


	//initialization
	setBatchMode(true);
	savefolder_root = loadfolder;


	//computation
	for (i=0; i<lengthOf(filenames); i++){
		filename = filenames[i];
	
		run("Close All");
	
		savefolder = savefolder_root + replace(filename,".czi","_singlechannel/");
		savefolder_rgb = savefolder_root + replace(filename,".czi","_rgb/");
		File.makeDirectory(savefolder);
		File.makeDirectory(savefolder_rgb);
		path = loadfolder + filename;
		
		convertCzi2SingleTiffs(path, savefolder, nr_ca_cycles, nr_frames_ca);
		singleChannel2Rgb(savefolder, savefolder_rgb);
		
		
	}
	setBatchMode(false);
}



function convertCzi2SingleTiffs(path, savefolder, nr_ca_cycles, nr_frames_ca){
		
	nr_modules = nr_ca_cycles * 2;  
	nr_channels = nr_ca_cycles * 5;

	//1st calcium timeseries
	module_nr_akt = 1;
	channel_nr_akt = 1;

	run("Bio-Formats Importer", "open=[" + path + "] color_mode=Default view=Hyperstack stack_order=XYCZT " + "series_" + module_nr_akt);
	getDimensions(width, height, channels, slices, frames);
	dataDimensionsCheck(nr_channels, nr_frames_ca);
	run("Duplicate...", "duplicate channels=1-2 frames=1-" + nr_frames_ca);
	run("Image Sequence... ", "format=TIFF name=" + module_nr_akt + "_ca save=" + savefolder);
	run("Close All");
	module_nr_akt++;
	channel_nr_akt = channel_nr_akt + 2;


	// following calcium timseries with specking image at the end
	while(module_nr_akt<nr_modules){
	
		run("Bio-Formats Importer", "open=[" + path + "] color_mode=Default view=Hyperstack stack_order=XYCZT " + "series_" + module_nr_akt);
		getDimensions(width, height, channels, slices, frames);
		dataDimensionsCheck(nr_channels, nr_frames_ca);
		run("Duplicate...", "duplicate channels=" + channel_nr_akt + "-" + channel_nr_akt+2 + " frames=1");
		run("Stack to Hyperstack...", "order=xyczt(default) channels=3 slices=1 frames=1 display=Color");
		run("Image Sequence... ", "format=TIFF name=" + module_nr_akt + "_sp_t001 save=" + savefolder);
		run("Close All");
	
		channel_nr_akt = channel_nr_akt + 3;
		module_nr_akt++;
		run("Bio-Formats Importer", "open=[" + path + "] color_mode=Default view=Hyperstack stack_order=XYCZT " + "series_" + module_nr_akt);
		getDimensions(width, height, channels, slices, frames);
		dataDimensionsCheck(nr_channels, nr_frames_ca);
		run("Duplicate...", "duplicate channels=" + channel_nr_akt + "-" + channel_nr_akt+1 + " frames=1-" + nr_frames_ca);
		run("Image Sequence... ", "format=TIFF name=" + module_nr_akt + "_ca save=" + savefolder);
		channel_nr_akt = channel_nr_akt + 2;
		module_nr_akt++;
		run("Close All");

		
	
	}

	// specking timeseries
	module_nr_akt = nr_modules;
	run("Bio-Formats Importer", "open=[" + path + "] color_mode=Default view=Hyperstack stack_order=XYCZT " + "series_" + module_nr_akt);
	getDimensions(width, height, channels, slices, frames);
	dataDimensionsCheck(nr_channels, nr_frames_ca);
	run("Duplicate...", "duplicate channels=" + nr_channels-2 + "-" + nr_channels +" frames=1-" + nr_frames_specking);
	run("Image Sequence... ", "format=TIFF name=" + module_nr_akt + "_sp save=" + savefolder);



}




function singleChannel2Rgb(loadfolder, savefolder){
	

	// get list of asc images
	reg = "[0-9]*_sp_t[0-9]{3}_c002\.tif";
	im_names = getFilteredFileList(loadfolder,reg);

	for (i=0;i<lengthOf(im_names);i++){
		//print(im_names[i]);
		name_ch1 = im_names[i]; //asc image name
		name_ch2 = replace(name_ch1, "c002.tif", "c003.tif");//brightfield image name
		print(name_ch1);
		print(name_ch2);
	
		//open asc image
		open(loadfolder + "/" + name_ch1);
		title_im1 = getTitle();
		setMinAndMax(0, 1250);//adjust brighness to hard value
		open(loadfolder + "/" + name_ch2);
		title_im2 = getTitle();
		getDimensions(width, height, channels, slices, frames);
		
		title_im3 = "im3";
		newImage(title_im3, "16-bit black", width, height, 1);
		
		
		run("Merge Channels...", "c1=" + title_im1 + " c2=" + title_im2 + " c3=" + title_im3 + " create ignore");
		run("RGB Color");
		
		savename = replace(name_ch1,"c002.tif", "rgb.tif");
		saveAs("Tiff", savefolder + savename);
		run("Close All");
	}


}

function getFilteredFileList(path,reg) {
//get a list of files from a given path, where each filename matches a given regular expression
//moehl 2014
	segNames = getFileList(path);
	n = 0;
	for (i=0;i<lengthOf(segNames);i++){
		if (matches(segNames[i],reg)){
			n++;
		}
	}
	
	namesSel = newArray(n); 
	nn = 0;
	for (i=0;i<lengthOf(segNames);i++){
		if (matches(segNames[i],reg)){
			namesSel[nn] = segNames[i];
			nn++;
		}	
	}

	return namesSel;
}






function createModuleSelector(nr_modules){

	module_selector = "";
	for (i=1; i<nr_modules+1; i++){
		module_selector = module_selector + "series_" + i + " ";
	}
	return module_selector;
}	



function dataDimensionsCheck(nr_channels, nr_frames_ca){
	getDimensions(width, height, channels, slices, frames);
	if(nrOfChannelsCheck(channels, nr_channels) && nrOfFramesCheck(frames, nr_frames_ca)){
		print("data dimensions ok");
		return true;		
	}
	else {
		print("data dimensions check failed");
		return false;
	}
	
	
	
}

function nrOfChannelsCheck(channels, nr_channels){
	if (nr_channels == channels){
		print("nr of channels check OK: " + channels);
		return true;
		else {
			print ("nr of channels check failed: " + nr_channels + " expected," + channels + " found.");
			return false;		 
		}
	}
	
}


function nrOfFramesCheck(frames, nr_frames_ca){
	if (nr_channels == channels){
		print("nr of frames check OK: " + frames);
		return true;
		else {
			print ("nr of frames check failed: " + nr_frames_ca + " expected," + frames + " found.");
			return false;		 
		}
	}
	
}





