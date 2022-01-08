# PackageDelivery
This program was designed to help optimize WGUPS deliveries using self-adjusting algorithms that will scale and adjust to their input. It was also designed with maintainability in mind for further adjustments as needed.

In this program, the Nearest Neighbor algorithm was used to determine the optimized delivery route for the manually-chosen groupings of packages on each truck. The algorithm is self-adjusting because it takes the package delivery addresses as input and determines an optimized delivery route on output. The implementation of this algorithm can be found as the deliver_to_nearest_neighbors method within the truck.py class.

Comments on the space-time complexity of major blocks of code can be found within the source code of this project. The space-time complexity of the entire program is O(n^3) due to line 65 through 70's multiple nested 'for' loops.

This program uses the Python 3.9 programming language. It was developed on a Windows 10 desktop PC using the JetBrains PyCharm 2021.2.2 IDE.
 
## Screenshots
![H](https://user-images.githubusercontent.com/54759532/148663766-66132ca6-b07e-447c-823a-29554707a2e5.jpg)
