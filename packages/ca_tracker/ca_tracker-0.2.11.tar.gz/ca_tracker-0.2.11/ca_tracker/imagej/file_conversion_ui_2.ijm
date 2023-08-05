//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//File Conversion for ca_tracker pipeline
//Image and Data Analysis Facility, Core Facilities, DZNE Bonn
//Author: Christoph Möhl
//Date: 30/06/2016
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 


macro "convert ca timeseries czi"{

	//folder selection cwith input files
	loadfolder = getDirectory("Choose Directory where czi files are located.");

	//parameter selection
	Dialog.create("convert czi timeseries to single tiffs");
  	Dialog.addNumber("number of ca modules (timeseries with live markers):", 4);
    Dialog.addNumber("number of frames per ca module:", 13);
    Dialog.addNumber("number of frames of final sp module (timeseries to monitor speck formation):", 41);
    Dialog.addNumber("number of channels in each ca module:", 2);
    Dialog.addNumber("number of channels in each sp module:", 4);
    Dialog.addNumber("asc channel in each sp module:", 3);
    Dialog.addNumber("brightfield channel in each sp module:", 4);
    Dialog.addCheckbox("Is the very first module a ca module, i.e. live marker time series? (leave unchecked if first module is a one-frame sp module with asc marker)", false);
    Dialog.show();
    
    nr_ca_cycles = Dialog.getNumber();
    nr_frames_ca = Dialog.getNumber();
    nr_frames_specking = Dialog.getNumber();
	nr_channels_ca = Dialog.getNumber();
	nr_channels_sp = Dialog.getNumber();
	asc_channel = Dialog.getNumber();
	brightfield_channel = Dialog.getNumber();
	start_with_ca = Dialog.getCheckbox();
	
	
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

		
		convertCzi2SingleTiffs(path, savefolder, nr_ca_cycles, nr_frames_ca, nr_channels_ca, nr_channels_sp, start_with_ca);
		
		singleChannel2Rgb(savefolder, savefolder_rgb, asc_channel, brightfield_channel);
		
		
	}
	setBatchMode(false);
}


function ImportSubStack(path, module_nr_akt, channel_lower, channel_upper, nr_frames){
	run("Bio-Formats Importer", "open=[" + path + "] color_mode=Default view=Hyperstack stack_order=XYCZT " + "series_" + module_nr_akt);
	//getDimensions(width, height, channels, slices, frames);
	//dataDimensionsCheck(nr_channels, nr_frames_ca);
	run("Duplicate...", "duplicate channels=" + channel_lower + "-" + channel_upper + " frames=1-" + nr_frames);
	
}

function ConvertModule(path, module_nr_akt, channel_lower, channel_upper, nr_frames, prefix, savefolder){
	
	ImportSubStack(path, module_nr_akt, channel_lower, channel_upper, nr_frames);
	nchannels = channel_upper - channel_lower + 1;
	run("Stack to Hyperstack...", "order=xyczt(default) channels="+ nchannels +" slices=1 frames=" + nr_frames + " display=Color");

	if (nr_frames == 1){
		run("Image Sequence... ", "format=TIFF name=" + module_nr_akt + "_" + prefix + "_t001 save=" + savefolder);
	}
	else {
		run("Image Sequence... ", "format=TIFF name=" + module_nr_akt + "_" + prefix + " save=" + savefolder);
		}
	run("Close All");	
}

function convertCzi2SingleTiffs(path, savefolder, nr_ca_cycles, nr_frames_ca, nr_channels_ca, nr_channels_sp, start_with_ca){

	if (start_with_ca) {
		//if the first module is ca, we have the same number of ca and sp modules	
		nr_modules = nr_ca_cycles * 2;  
		nr_channels = nr_ca_cycles * (nr_channels_ca + nr_channels_sp);
	}
	else {
		//if the first module is sp, we have one more sp module than ca modules
		nr_sp_cycles = nr_ca_cycles + 1;
		nr_modules = nr_ca_cycles + nr_sp_cycles; 
		nr_channels = nr_sp_cycles * nr_channels_sp + nr_ca_cycles * nr_channels_ca;
		}
	
	//1st calcium timeseries
	module_nr_akt = 1;
	channel_nr_akt = 1;


	if (start_with_ca) {
		//if first module is ca module
		ConvertModule(path, module_nr_akt, channel_nr_akt, nr_channels_ca, nr_frames_ca, "ca", savefolder);
		module_nr_akt++;
		channel_nr_akt = channel_nr_akt + nr_channels_ca;
	
	
		// following calcium timseries with specking image at the end
		while(module_nr_akt<nr_modules){
			start_ch = channel_nr_akt;
			stop_ch = channel_nr_akt + nr_channels_sp - 1;
			nr_frames = 1;
			ConvertModule(path, module_nr_akt, start_ch, stop_ch, nr_frames, "sp", savefolder);
			
			channel_nr_akt = channel_nr_akt + nr_channels_sp;
			module_nr_akt++;
			
			start_ch = channel_nr_akt;
			stop_ch = channel_nr_akt + nr_channels_ca - 1;
			nr_frames = nr_frames_ca;
			ConvertModule(path, module_nr_akt, start_ch, stop_ch, nr_frames, "ca", savefolder);
			
			channel_nr_akt = channel_nr_akt + nr_channels_ca;
			module_nr_akt++;
			
		}
	}

	else{
		//if fist module is sp module
		// following calcium timseries with specking image at the end
		while(module_nr_akt<nr_modules){
			start_ch = channel_nr_akt;
			stop_ch = channel_nr_akt + nr_channels_sp - 1;
			nr_frames = 1;
			ConvertModule(path, module_nr_akt, start_ch, stop_ch, nr_frames, "sp", savefolder);
			
			channel_nr_akt = channel_nr_akt + nr_channels_sp;
			module_nr_akt++;
			
			start_ch = channel_nr_akt;
			stop_ch = channel_nr_akt + nr_channels_ca - 1;
			nr_frames = nr_frames_ca;
			ConvertModule(path, module_nr_akt, start_ch, stop_ch, nr_frames, "ca", savefolder);
			
			channel_nr_akt = channel_nr_akt + nr_channels_ca;
			module_nr_akt++;
			
		}
		
	}
	
	
	// specking timeseries
	module_nr_akt = nr_modules;

	start_ch = nr_channels-nr_channels_sp+1;
	stop_ch = nr_channels;
	nr_frames = nr_frames_specking;
	ConvertModule(path, module_nr_akt, start_ch, stop_ch, nr_frames, "sp", savefolder);
	



}




function singleChannel2Rgb(loadfolder, savefolder, asc_channel, brightfield_channel){
	

	// get list of asc images
	reg = "[0-9]*_sp_t[0-9]{3}_c001\.tif";
	im_names = getFilteredFileList(loadfolder,reg);

	for (i=0;i<lengthOf(im_names);i++){
		//print(im_names[i]);
		//name_ch1 = im_names[i]; //asc image name
		name_ch1 = replace(im_names[i], "c001.tif", "c00" + asc_channel + ".tif"); //asc image name	
		name_ch2 = replace(im_names[i], "c001.tif", "c00" + brightfield_channel + ".tif");//brightfield image name
		print(name_ch1);
		print(name_ch2);
	
		//open asc image
		open(loadfolder + "/" + name_ch1);
		title_im1 = getTitle();
		//run("Enhance Contrast", "saturated=0.0 normalize");
		setMinAndMax(0, 900);//adjust brighness to hard value
		
		//open brightfield image
		open(loadfolder + "/" + name_ch2);
		title_im2 = getTitle();
		run("Enhance Contrast...", "saturated=0.3 normalize");
		getDimensions(width, height, channels, slices, frames);
		
		title_im3 = "im3";
		newImage(title_im3, "16-bit black", width, height, 1);
		
		
		//run("Merge Channels...", "c1=" + title_im3 + " c2=" + title_im2 + " c4=" + title_im1 + " create");
		//run("Merge Channels...", "c1=" + title_im1 + " c2=" + title_im2 + " c4=" + title_im3 + " create ignore");
		run("Merge Channels...", "c1=" + title_im3 + " c2=" + title_im2 + " c4=" + title_im1 + " create");
		run("RGB Color");
		
		savename = replace(name_ch1, "c00" + asc_channel + ".tif", "rgb.tif");
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





