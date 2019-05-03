#ifndef MIR_TEMPLATE_MATCHING_TEMPLATE_MATCHING_ROS_H
#define MIR_TEMPLATE_MATCHING_TEMPLATE_MATCHING_ROS_H

// OpenCV
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <cv_bridge/cv_bridge.h>

// Messages
#include <sensor_msgs/image_encodings.h>
#include <mcr_perception_msgs/ImageList.h>
#include <std_msgs/String.h>

#include <ros/ros.h>

class TemplateMatchingROS
{
private:
    ros::Subscriber sub_event_in_;
    ros::Subscriber sub_camera_img_;
    ros::Subscriber sub_object_img_list_;

    void eventInCallback(const std_msgs::String::ConstPtr &msg);
    void imageCallback(const sensor_msgs::ImageConstPtr &image);
    void imageListCallback(const mcr_perception_msgs::ImageList &msg);
    
    ros::NodeHandle nh_;

    cv::Mat img, template_img, result, img_display;

    int match_method, result_cols, result_rows;
    const char* image_window;
    const char* result_window;
    double minVal, maxVal; 
    cv::Point minLoc, maxLoc, matchLoc;
    bool event_msg_received_;
    bool img_list_received_;

public:
    TemplateMatchingROS();
    virtual ~TemplateMatchingROS();

    void update();
};

#endif // MIR_TEMPLATE_MATCHING_TEMPLATE_MATCHING_ROS_H