#pragma once
#include <vector>
#include <filesystem>
#include <opencv2/opencv.hpp>
#include "Channel.h"

class Compresser {

    public:
        Compresser(const std::string &file);
        void loadImage(const std::string &file);
        void loadChannels(const std::string &file);
        void saveImage(const std::string &file);
        void saveChannels(const std::string &file);
        void compose(double k);
    private:
        cv::Mat image;
        std::vector<Channel> channels;

};
