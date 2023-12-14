#pragma once
#include <vector>
#include <filesystem>
#include <opencv2/opencv.hpp>
#include "Channel.h"

class Compresser {

    public:
        Compresser(std::string file);
        void loadImage(std::string file);
        void saveImage(std::string file);
        void saveChannels(std::string file);
        void compose(double k);
    private:
        cv::Mat image;
        std::vector<Channel> channels;

};
