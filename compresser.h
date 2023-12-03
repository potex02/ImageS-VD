#pragma once
#ifndef COMPRESSER_H
#define COMPRESSER_H
#include<opencv2/opencv.hpp>

class Compresser {

    public:
        Compresser(std::string path);
        cv::Mat getImage();
        cv::Mat compress(int k);
    private:
        cv::Mat image;

};

#endif // COMPRESSER_H
