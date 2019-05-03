#include <mir_template_matching/template_matching_ros.h>

#include <iostream>

TemplateMatchingROS::TemplateMatchingROS():
  nh_("~"),
  match_method(0),
  image_window("Source Image"),
  result_window("Result window"),
  event_msg_received_(false),
  img_list_received_(false)
{
  //Subscribers
  sub_event_in_ = nh_.subscribe("event_in", 1, &TemplateMatchingROS::eventInCallback, this);
  sub_camera_img_ = nh_.subscribe("camera_img", 1, &TemplateMatchingROS::imageCallback, this);
  sub_object_img_list_ = nh_.subscribe("object_img_list", 1, &TemplateMatchingROS::imageListCallback, this);
}

TemplateMatchingROS::~TemplateMatchingROS()
{
  sub_event_in_.shutdown();
  sub_camera_img_.shutdown();
  sub_object_img_list_.shutdown();
}

void TemplateMatchingROS::eventInCallback(const std_msgs::String::ConstPtr &msg)
{
  event_msg_received_ = true;
}

void TemplateMatchingROS::imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  ROS_INFO("[mir_template_matching] Received image ");

  try {
    img = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8)->image;
  } catch (cv_bridge::Exception& e) {
    ROS_ERROR("cv_bridge exception: %s", e.what());
  }
}

void TemplateMatchingROS::imageListCallback(const mcr_perception_msgs::ImageList& msg)
{
  if (! img_list_received_)
  {
    ROS_INFO("[mir_template_matching] Received image list ");

    try {
      template_img = cv_bridge::toCvCopy(msg.images[0], sensor_msgs::image_encodings::BGR8)->image;
    } catch (cv_bridge::Exception& e) {
      ROS_ERROR("cv_bridge exception: %s", e.what());
    }

    img_list_received_ = true;
  }
}

void TemplateMatchingROS::update()
{
  if (event_msg_received_)
  {
    img.copyTo( img_display );
    result_cols =  img.cols - template_img.cols + 1;
    result_rows = img.rows - template_img.rows + 1;
    result.create(result_rows, result_cols, CV_32FC1);
    cv::matchTemplate(img, template_img, result, match_method);
    cv::normalize(result, result, 0, 1, cv::NORM_MINMAX, -1, cv::Mat());

    cv::minMaxLoc(result, &minVal, &maxVal, &minLoc, &maxLoc, cv::Mat());
    if( match_method  == cv::TM_SQDIFF || match_method == cv::TM_SQDIFF_NORMED )
      { matchLoc = minLoc; }
    else
      { matchLoc = maxLoc; }

    std::cout << "Matching point is: " << matchLoc << std::endl;

    cv::rectangle( img_display, matchLoc, cv::Point( matchLoc.x + template_img.cols , matchLoc.y + template_img.rows ), cv::Scalar::all(0), 5, 8, 0 );
    cv::rectangle( result, matchLoc, cv::Point( matchLoc.x + template_img.cols , matchLoc.y + template_img.rows ), cv::Scalar::all(0), 5, 8, 0 );

    cv::imshow( image_window, img_display );
    cv::imshow( result_window, result );
    cv::imshow( "Template", template_img );
    cv::waitKey(0);
  }
}
