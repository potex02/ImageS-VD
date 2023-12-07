#pragma once
#include<vector>
#include<opencv2/opencv.hpp>
#include "Channel.h"

class Compresser {

    public:
        Compresser(std::string path);
        cv::Mat getImage();
        void decompose();
        cv::Mat compose(double k);
    private:
        cv::Mat image;
        std::vector<Channel> channels;

};
