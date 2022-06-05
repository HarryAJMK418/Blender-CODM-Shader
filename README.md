# Blender-BC5-XY-Normal-Converter
This addon is created to add a node group to the shader editor in Blender which can help to convert the BC5/XY Normal textures used in certain games to Tangent Space Normal Map and separates the additional texture present in blue channel of the raw texture.


# How to install?
1. Go to Edit > Preferences > Add-ons 
2. Click on Install
3. Select the file bc5xy_normal_addon_v.v.v.zip
4. Click on Install Add-on
5. Enable the Add-on

# How to use the addon?
When this addon is installed, it automatically adds the node group along with other nodes in Shader Nodes. Just like you add other nodes, You can add this one too.

Here is a video demonstrating how to add the node in shader editor

https://user-images.githubusercontent.com/83151920/172041496-116eeb2c-bade-4980-9c5b-217d2196e966.mp4

# Details:-
![image](https://user-images.githubusercontent.com/83151920/172041554-412d2c92-d54a-496f-b381-ea8c6add780e.png)

A. Input:-
   
   XY Normal Map:- This is where you have to connect the BC5/XY Normal map
   
   Normal Strength:- This sets the Strength of fixed Normal map. Only works for the vector output "Normal"
   
   Invert Blue:- in Some games, they store some texture in the blue channel of BC5 compressed Textures. In that case if the texture need inversion, then change            the value from 0 to 1.
   
B. Output:- 
   
   Normal map:- The fixed Normal map as texture
   
   Normal:- The Fixed Normal map as vector.
   
   Blue Channel:- if any additional texture is present in the blue channel of BC5 compressed, then this is the output. Generally Roughness/Smoothness is stored(if).


# Compatibility:-
This addon is compatible with Blender 3.0+ and tested in blender 3.0,  3.1.0

# License:-
MIT License

Copyright (c) 2022 CODcDevil


# Further info:-
This is my first addon in blender so theres a large amount of chance of causing an error. If you face any error, then create an issue or contact me in Discord. My Discord name is :-  COD©Devil#2334
