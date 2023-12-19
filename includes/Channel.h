#pragma once
#include <iostream>
#include <opencv2/opencv.hpp>

class Channel {

    public:
        Channel(const cv::Mat &matrix);
        Channel(const cv::Mat &_u, const cv::Mat &_w, const cv::Mat &_vt);
        void save(cv::FileStorage &fs, int i);
        cv::Mat compose(double k);
    private:
        cv::Mat u;
        cv::Mat w;
        cv::Mat vt;

};
