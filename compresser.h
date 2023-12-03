#pragma once
#ifndef COMPRESSER_H
#define COMPRESSER_H
#include<opencv2/opencv.hpp>

class Compresser {

    public:
        Compresser(std::string path);
        cv::Mat compress(int k);
        cv::Mat image;

};

#endif // COMPRESSER_H
