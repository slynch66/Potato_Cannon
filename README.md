# Potato_Cannon

## Table of Contents
* [Project Proposal](#Planning)
---

## Planning

### Design + How it works

<img src="https://raw.githubusercontent.com/slynch66/Potato_Cannon/main/Images/Cannon-Planning.jpg" width = 500 height = 700\>

<img src="https://raw.githubusercontent.com/slynch66/Potato_Cannon/main/Images/potato-cannon-circuit-planning.jpg" width = 500 height = 700\>

### Materials

4" PVC pipe cut to 18 inches long
4" PVC threaded coupler
4" PVC cleanout cap
4" to 2" PVC adapter
2" PVC pipe cut to 3 feet long
1" PVC pipe cut to 4 inches for the sparker

Ramrod of some sort

PVC primer
PVC cement

Manual grill sparker

---

### Payload/Testing

#### Achieving maximum power

At first we'll need to test the optimum number of seconds to spray hairspray in the combustion chamber. What number of seconds will generate maximum combustion and force behind the potato/raspberrypi?

More hairspray doesn't always mean more power, because the energy equation is  'more energy = more air + more fuel' and with more hairspray, eventually not all of it will combust due to a lack of air. In order to test how many seconds generates the most speed and force of the pi in the sky, we will use a stopwatch and track the time it takes for the projectile to travel a set distance.

---

### What will the Raspberry Pi do?

The pi will measure acceleration values as it is fired and travels through the air. The raspberry pi will be in a projectile that is cylindrical in shape, because the pi is longer than the barrel diameter, but not as wide as the barrel diameter.

---

### Pseudocode

<img src="https://raw.githubusercontent.com/slynch66/Potato_Cannon/main/Images/Potato-Cannon-Pseudocode.jpg" width = 500 height = 700\>

---

### Timeline - 6 Weeks

#### First two weeks (2/1/22 - 2/15/22)

   1. Build the cannon 
  
   2. Build the ignition mechanism
         - Make sure after the hole(s) is drilled for the sparker wire(s) that the hole is effectively sealed so that the force created in the combustion chamber doesn't                   exit out of the "sealed" ignition hole.

#### Second two weeks (2/17/22 - 3/3/22)
        
   3. Test for the optimum amount of hairspray.
        
   4. Design and build a shell to encase the raspberry pi as it is fired from the cannon and protect it from impact

#### Third two weeks (3/4/22 - 3/18/22)
     
   5. Test the raspberry pi with the projectile to collect acceleration values and complete the project requirements
        
   6. Find ways to make the design better to increase accuracy, velocity, etc.

#### Post-Project
   
   After finishing the Potato Cannon project, we would build off of what we learned to make a mortar launcher tube. We would build it to shoot like tennis balls or potatoes or something, and you would be able to change the angle of the tube and the force of the launch to hit different distance targets.
   
---

### Risk Mitigation

Safety Test Plan -->   First of all, we need to make sure the potato cannon won't explode when it's fired. For the first few tests, we will fire the potato cannon from a distance of at least 15 feet with an obstacle between us and the cannon, until we can be sure of its structural integrity while using increasing amounts of hairspray. For the rest of the tests when we're operating the cannon as it is fired, we will not differ from using the amount of hairspray that was safely tested from a distance.
   
   We will wear safety glasses when we fire the potato cannon, and we'll only fire it outside (obviously) with some open space. For example, we could test it on the field next to the baseball field. We would aim at things with a background of the hill towards Melbourne.
   
   The hairspray will either be transported to and from school, or it will be stored in a secure place at school so that only we can fire it, and no one can just "try it" during the day.

---

### 2/3/22

PVC pipe schedule 40 whether the inside is solid wall or cellulose core will withstand the pressures of the potato cannon.

Mr Dierolf has a powerful BBQ grill sparker that we can use for the potato cannon. We will drill two small holes for the power/ground wires from the sparker, spaced a half-inch (or slightly less) apart. The wires have diameters of 4mm, and any tiny gaps with the wires in the holes can be filled with a regular sealant like caulk or silicone.

### 2/6/22 Testing

I brought the cannon home over the weekend and finished putting it together. At first I didn’t spray enough hairspray (I was doing about 2-3 seconds worth), and then I used around 5 seconds worth of hairspray and I sounded like a rocket launch.

![at-home-test-gif](https://raw.githubusercontent.com/slynch66/Potato_Cannon/main/Images/under25MBatHomeTest.gif)

### First-time CHS Test

We went out to the field and tested the potato cannon using potatoes as projectiles. We measured the speed of the projectiles in feet-per-second, and I believe it was around 80 miles an hour.

### First Potato Cannon Shell

We finished printing the first model of our potato cannon shell. We went to test the shell out and put a bag of screws and bolts in it. This would simulate the weight of the circuit components. The weight was not secured inside of the shell, and it broke the shell when it was launched. From our first launch we learned that our shell design was too thin and weak in a few areas, and so we beafed it up in our next design. We thickened the outside of the shell and the L-arms that would hold the raspberry pi. We also thickened the arm that would hold the servo.

### Second Potato Cannon Shell

<img src="https://raw.githubusercontent.com/slynch66/Potato_Cannon/main/Images/potato-cannon-shell.jpg" width = 500 height = 700\>

After we changed the thickness of the parts mentioned above, we printed the second version of the shell. Some additional updates from the first shell included a screw-on design for the shell cap and the servo mount extended to contact both sides of the inner shell. The second shell had rings to tie the parachute to, so that we could make sure the shell gently descended to the ground after launch.

#### Servo Lock and Parachute Release Mechanisms

##### Purpose of the servo lock mechanism

The servo lock mechanism secures the nose cone of the shell to the main cylinder. Before launch and after we pack the parachute into the nose cone, we press a button the servo turns to lock the nose cone against the main cylinder. When we press the final launch button, after a certain amount of time (35 seconds for the final version of the code) the servo turns and releases the main cylinder from the nose cone, which falls away. As the nose cone and main body seperate, the parachute is tugged out of the nose cone and deploys. The cone is light and thick enough to hit the grass and be ok, but the parachute softly lands the much heavier main cylinder.

When messing with the nose cone, we realized the servo lock mechanism was too bulky for the parachute to easily escape. We changed the CAD design of the cone to only have one less bulky shelf for the servo arm to lock with.

<img src="https://raw.githubusercontent.com/slynch66/Potato_Cannon/main/Images/nose-cone.jpg" width = 500 height = 700\>

The second and final nose cone had a more efficient servo lock mechanism and it was longer than the first version with a length of 4in. This would be enough to store the parachute and its string without having to pack it down very much to fit. If we had to pack it down, the release of the nose cone wouldn't have enough force to deploy the parachute.

When we were packing the parachute into the nose cone, it was really tough because of how long the string was for the parachute. The parachute had 3 loops of string attached, and we shortened each loop by 3 inches. This length still allowed the parachute to deploy, and it was much easier to pack.

### Code development

*Need to input more here.

### Testing in May

With the second and improved shell, we s

Go over testing, having the hole wrong for the pi communication port, and changes we made to the parachute string and cannon itself. Go over project optimization with the length of wait time for the final launch button and the number of seconds of hairspray we used.
