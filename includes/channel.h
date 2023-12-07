#pragma once
#include<iostream>
#include<opencv2/opencv.hpp>

class Channel {

    public:
        Channel(cv::Mat matrix);
        cv::Mat compose(double k);
    private:
        cv::Mat u;
        cv::Mat w;
        cv::Mat vt;

};
