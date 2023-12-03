#include "Compresser.h"
#include<iostream>

Compresser::Compresser(std:: string path) {

    this->image = cv::imread(path);
    this->image.convertTo(this->image, CV_64F);
    if(this->image.empty()) {

        throw new std::exception();

    }

}
