# Lab 1 Report

Members:
- Rohan Gupta
- Matthew Hong
- Harshitha Rajaprakash
- Scott Susanto

## Section 4

ROS installation verified.

## Section 5

cs545_lab1 package successfully created.

## Section 6

Running `rqt_graph`, we notice 2 nodes, `/teleop_turtle` and `/turtlesim`, and an arrow from `/teleop_turtle` to `/turtlesim` with the label `/turtle1/cmd_vel`. Using the idea of Bayes' Nets, this suggests a dependency of the `/turtlesim` state from the `/teleop_turtle` state.

`rosservice`: a set of tools for querying various ros services
`rostopic`: a medium for nodes to exchange messages for a particular subject
`rosparams`: configs for interacting with the Parameter Server
`rosbag`: a set of tools that records and plays back ros topics

## Section 7

Everything working as expected, [video demo](https://drive.google.com/file/d/1xpAFPIQZcHOfVomi4CVa_vThvyoGrsRO/view?usp=drive_link) here.

## Section 8

### Resources Consulted

- [rosservice](https://wiki.ros.org/rosservice)
- [rostopic](https://wiki.ros.org/rostopic)
- [rosparam](https://wiki.ros.org/rosparam)
- [rosbag](https://wiki.ros.org/rosbag)
- [Publisher & Subscriber](https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)

As to how we used these, we just read documentation.

### Contributions

- Rohan and Scott: Wrote publisher code (~50%)
- Matthew and Harshitha: Wrote subscriber code (~50%)
