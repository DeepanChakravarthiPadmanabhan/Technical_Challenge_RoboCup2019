#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <iostream>
using namespace std;
using namespace cv;
Mat img, templ,result;
int match_method=0;
void MatchingMethod();
int main( int argc, char** argv )
{
  img = imread( argv[1], IMREAD_COLOR );
  templ = imread( argv[2], IMREAD_COLOR );

  if(img.empty() || templ.empty())
  {
    cout << "Can't read one of the images" << endl;
    return -1;
  }

  MatchingMethod();

  waitKey(0);
  return 0;
}
void MatchingMethod()
{

  int result_cols =  img.cols - templ.cols + 1;
  int result_rows = img.rows - templ.rows + 1;
  result.create( result_rows, result_cols, CV_32FC1 );
  matchTemplate( img, templ, result, match_method);
  normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );
  double minVal; double maxVal; Point minLoc; Point maxLoc;
  Point matchLoc;
  minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );
  if( match_method  == TM_SQDIFF || match_method == TM_SQDIFF_NORMED )
    { matchLoc = minLoc; }
  else
    { matchLoc = maxLoc; }
  cout<<"Match location\n"<<matchLoc;

  return;
}
//https://docs.opencv.org/3.4/de/da9/tutorial_template_matching.html