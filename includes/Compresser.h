#pragma once
#include <vector>
#include <algorithm>
#include <filesystem>
#include <opencv2/opencv.hpp>
#include "Channel.h"

class Compresser {

    public:
        static std::vector<std::string> supportedExtensions;
        static inline bool isImage(const std::string &file);
        Compresser(const std::string &file);
        void loadImage(const std::string &file);
        void loadChannels(const std::string &file);
        void saveImage(const std::string &file);
        void saveChannels(const std::string &file);
        void compose(double k);
    private:
        cv::Mat image;
        std::vector<Channel> channels;
        cv::Mat convertToPgm();

};
