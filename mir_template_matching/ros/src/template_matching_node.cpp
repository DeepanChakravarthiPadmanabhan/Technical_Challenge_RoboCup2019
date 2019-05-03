#include <mir_template_matching/template_matching_ros.h>

int main( int argc, char** argv )
{
  ros::init(argc, argv, "template_matching");
  ros::NodeHandle nh("~");
  ROS_INFO("[template_matching] node started");

  int frame_rate = 30; // in Hz
  TemplateMatchingROS template_matching_ros_;

  ros::Rate loop_rate(frame_rate);

  while (ros::ok())
  {
    template_matching_ros_.update();
    loop_rate.sleep();
    ros::spinOnce();
  }
  return 0;
}
