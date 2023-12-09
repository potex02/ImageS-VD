#pragma once
#include<vector>
#include<opencv2/opencv.hpp>
#include "Channel.h"

class Compresser {

    public:
        Compresser(std::string path);
        void save();
        cv::Mat compose(double k);
    private:
        std::vector<Channel> channels;

};
