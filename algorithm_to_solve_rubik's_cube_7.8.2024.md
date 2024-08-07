# Algorithm to solve Rubik’s Cube

[Source](https://www.geeksforgeeks.org/algorithm-to-solve-rubiks-cube/)

A Rubik’s Cube is an interesting puzzle invented by ‘Erno Rubik’ which has 43 quintillion possible configurations. But with the use of certain algorithms, it can be solved easily. There are many variations of the Rubix cube nowadays but the most basic one is the 3x3x3 Rubik’s cube.

A 3x3x3 Rubik’s cube is made by joining 21 pieces: 

- 1 principle piece with three axles
- 8 corner pieces (corner solid shapes) with three tones
- 12 edge pieces (edge 3D squares) with two tones

**Centerpieces are always at their original position only.**

## Basic Rotations Of Rubik’s Cube:

- R: Rotate the right layer clockwise.
- R’: Rotate the right layer anti-clockwise.
- L: Rotate the left layer clockwise.
- L’: Rotate the left layer anti-clockwise.
- U: Rotate the top layer clockwise.
- U’: Rotate the top layer anti-clockwise.
- F: Rotate the front layer clockwise.
- F’: Rotate the front layer anti-clockwise.

## Beginners Method:

The easy solution to solve a Rubik’s cube is to follow the approach to first solve the bottom layer, then the middle layer, and then finally the top layer.

Step 1: 
First choose a centerpiece of any color (say white) and then make a white cross by bringing all the four edge pieces adjacent to the white center.

Step 2:  
Match colors of all four centerpieces of the lateral face with the edges of the bottom layer one by one and sending the matched pairs in opposite directions and then bringing them again to make a cross of white.

Step 3: 
Set corners of the bottom layer by first matching the correct corner matching its desired color. Then apply the algorithm R U R’ U’ and repeat the same algorithm till the bottom corner piece is set at its correct position...

Step 4: 
Make the second layer by matching all four edges at the lateral faces. First, match the color of the top layer edge with its center layer and observe the other part of the piece i.e top facing color.

Case 1: If the other part color matches with the centerpiece at the right side, then apply the algorithm  U R U’ R’ U’ F’ U F.

Case2:  If the other part color matches with the centerpiece at the left side, then apply the algorithm   U’ L’ U L U F U’ F’.

Step 5:
Make the yellow cross on the top layer by applying the simple algorithm  F R U R’ U’ F’  1-3 times...

Step 6: 
Now match any one edge of the top layer with the centerpiece in the middle layer, and then apply the algorithm F R U R’ U’ F’ until all the edges are matched.

Step 7:  
Now to match all the corner pieces on the top layer, first see the corner which is already being matched and keep it as the front face and towards the right. If none of the corner pieces are in the right place, you can hold the cube in any orientation with the unmatched pieces on top and apply the algorithm U R U’ L’ U R’ U’ L.

Step 8: 
In the final step keep yellow as the front face and start from any corner apply the algorithm U R’ U’ R until the corner arranges correctly, then rotate the top layer to bring another disarranged corner on the top right side and repeat U R’ U’ R algorithm again to arrange it, and so on. After arranging all the corner pieces, just move the yellow facing layer 1-2 times if needed to completely solve your cube.  

With this final step, the Rubik’s cube is finally solved.



