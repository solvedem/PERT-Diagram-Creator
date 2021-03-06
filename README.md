# PERT-Diagram-Creator

[![pert2.jpg](https://s17.postimg.org/ttsleeh67/pert2.jpg)](https://postimg.org/image/p7wh61vmz/)

Dependencies: Python 2 or 3

## Getting started:

Download Files

Run pert_.py

A blank screen with some shapes and buttons will appear.

[![pert3.jpg](https://s17.postimg.org/uxcpqdh8v/pert3.jpg)](https://postimg.org/image/9axp9ciob/)

The program assumes a left-to-right network, so the first big circle (on the left) represents the starting point for the project, and the one on the right represents the end of the project.

The left circle will connect arrows to all project nodes with no dependencies, as they represent the first
steps of the project.

The right circle will connect arrows to all project nodes that no other nodes depend on, as they represent the last
steps of the project.

The big square in the bottom right represents the evaluate and quit button.

The small square above the right circle respresents the "Next" button, which will be further described later.

## Using the Program

#### Step 1: Creating Nodes

Every node on the network will represent a task and will hold the time it takes to complete that task.

The first step for the user is drawing each node on the network, and filling in their times.

To do this, the user clicks on the blank window where they desire a node to be. The program then 
displays an input box for the user to enter time for that node.

[![pert4.jpg](https://s17.postimg.org/8b7ed23cf/pert4.jpg)](https://postimg.org/image/iy17ihbhn/)

After a number is in the entry box, the user clicks elsewhere on the window to be done with the current node.

With another click, they can repeat the process and add another node.

[![pert5.jpg](https://s17.postimg.org/jasloo973/pert5.jpg)](https://postimg.org/image/i8if64qdn/)

Step 1 summary:

1. User clicks where they want a node.
2. User types in number representing time for node's task to be completed.
3. User clicks elsewhere on window to submit this number and draw the node.
4. User repeats process until they don't want any more nodes in their network.

[![pert6.jpg](https://s17.postimg.org/r3j9grhrz/pert6.jpg)](https://postimg.org/image/fr6nyz92z/)

To move onto step 2, the user will click the "next" button, located above the circle on the right.
It will be filled with color when it has been clicked.

#### Step 2: Drawing Arrows

Arrows will help represent the network and establish dependencies and the critical path.

After the user clicks the next button, they can draw their arrows. 

This step might seem self explanatory.

The user clicks two circles, as desired. 
The first circle the user clicks will depend on the second.

For example, in this network, Node b was clicked first, then Node d.

[![pert7.jpg](https://s17.postimg.org/6w5tomzrz/pert7.jpg)](https://postimg.org/image/4eu2hdfvf/)

This process can be repeated until the evaluation button is clicked.

Before evaluation button is clicked:

[![pert8.jpg](https://s17.postimg.org/n8fve4lqn/pert8.jpg)](https://postimg.org/image/3ql7y6osr/)

After evaluation button is clicked:

[![pert9.jpg](https://s17.postimg.org/6kodbpja7/pert9.jpg)](https://postimg.org/image/67wz5j10b/)

#### Final Output:

The critical path's nodes will be highlighted in blue. The time it takes to for a given node to 
be completed from the start of the project is shown to the lower left of each node.

Click the button in the buttom right to quit.

#### Note:

When drawing arrows, the program will not be affected by any clicks outside of a circle. However, the program will allow you to make illogical diagrams. Examples of these include arrows pointing backwards, circular projects, nodes that point to themselves, etc. If a logical evaluation is desired, a logical diagram must be drawn. However, feel free to push the boundaries looking for improvements.
