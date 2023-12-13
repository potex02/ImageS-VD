#pragma once
#include<vector>
#include<opencv2/opencv.hpp>
#include "Channel.h"

class Compresser {

    public:
        Compresser(std::string path);
        void saveImage(std::string p);
        void saveChannels(std::string p);
        void compose(double k);
    private:
        cv::Mat image;
        std::vector<Channel> channels;

};
