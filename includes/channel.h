#pragma once
#include<opencv2/opencv.hpp>

class Channel {

    public:
        Channel(cv::Mat _matrix);
        void decompose();
        cv::Mat compose(double k);
    private:
        cv::Mat matrix;
        cv::Mat u;
        cv::Mat w;
        cv::Mat vt;

};
