#pragma once
#include<opencv2/opencv.hpp>

class Channel {

    public:
        Channel(cv::Mat _matrix);
        cv::Mat compress(int k);
    private:
        cv::Mat matrix;
        cv::Mat u;
        cv::Mat w;
        cv::Mat vt;

};
