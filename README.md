
![Animation3](https://github.com/Srothency/CorporateClash_FishingBot/assets/27137875/65f4318e-cb5f-4601-b674-a0dfde8f1631)


# How it Works  

    1.) Crop the image along our boundary that we manually defined
    2.) Create a binary BW image based on a tweaked threshold
    3.) Find the center biggest "region" in the BW image
    4.) Apply our linear regression model based on the center of that region
    5.) click on the cast button, move the cursor the calculated location, then release.
    6.) Wait 1.75sec before casting again


# Calibrating the Bot 
TODO: Make this less terrible

  Because the model was tuned for the dock closest to Polar Place in the brrgh, you may need to adjust it if attempting to use it in other locations. This means:
  
    1.) Update the Fishing Boundaries
        - Make the box cover the water and avoid having anything in the box darker than the fish shadows.
    2.) Update the Region Threshold
        - We want the fish shadows to be as big as possible without also introducing other elements into the scene.
        - update the line "get_bw_region(123)" in the fish() function.
    3.) Collect Data
        - Cast your line multiple times into the water manually then running calibrate with **F10**.
        - The PNGs store the X/Y coordintes of the location where your mouse cursor was
        - You will then need to manually locate the X/Y coordintes of the resulting bobber. I just use MS paint for this.
    4.) Create the linear model. 
        - Store the resulting values within the mouse_x,mouse_y,fish_x,fish_y variables within the createModel.py script
        - Run the createModel script with your new data.
    5.) Update the function "calculate_cast" within main.py

# Starting the bot
  Run main.py and then press **F12** to start the bot. it will work best on the dock closest to Polar place.

