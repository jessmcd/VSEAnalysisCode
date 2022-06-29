
To start, create a CSV with sticknet ID, date, location, estimated TOA, and type (R: rotating, NR: non-rotating, T: tornadic). You may want to consider adding the closest radar site for each sticknet as well. 

1. Find TOA using the code in 1Hz_analyses.ipynb
2. Calculate storm motion using Storm_motion_algorithm.ipynb (note, this file has been cleaned up and generalized, so you'll need to add in code to loop over the CSV data and save it to the CSV. See the 1Hz_analyses script for examples if you need help. You'll also need to figure out how best to manually grid the radar data so that it's on a 1-km grid). 
3. Manually determine storm reflectivity angle
4. Run the code for calculating deficits and gradients in 1Hz_analyses.ipynb


the 1Hz_PubPlots contains the code for most of my paper figures. PubPlots_ReflecStormLifecycle is a mess but might be useful. the basic code in the 10Hz_to_1Hz script is probably already in stuff you have (like the QC scripts) but I included it anyways. 



A quick description of what is in the CSV file I gave you:
date = event date
ID = "0XXXA"
N_ID = the 4 letter identifier we gave sticknets in VSE and meso18-19
Lats/Lons = you know lol
mode = storm mode
type = R: rotating, NR: non-rotating, T: tornadic
TOA = finalized time of arrival
storm_ref_angle = the manually calculated reflectivity angle (see Fig. 3 from my paper, the difference between the 0deg line and the black dashed line (negative angle typically)
Ua and Va = the storm motion vectors that came from Step 2. 
TOA_mods and Bsdist_mods = notes to myself about which sticknets had manually altered methods
TE_dist, TV_dst, and dTVdn = the thetae deficits, thetav deficits, and thetav gradients, respectively
storm_u_OLD and storm_v_OLD = kinda self explanatory, ignore. 
TE_BS, TV_BS, and Tdd_BS = base state values from TE, TV, and Tdd (dewpoint depression) that I used for other analyses. 