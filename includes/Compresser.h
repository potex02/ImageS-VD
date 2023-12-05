#pragma once
#include<opencv2/opencv.hpp>
#include "Channel.h"

class Compresser {

    public:
        Compresser(std::string path);
        cv::Mat getImage();
        cv::Mat compress(double k);
    private:
        cv::Mat image;
        std::vector<Channel> channels;

};
