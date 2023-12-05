#include "channel.h"
#include<iostream>

Channel::Channel(cv::Mat _matrix) {

    this->matrix = _matrix;

}
void Channel::decompose() {

    double min, max;
    cv::SVD svd;

    svd.compute(this->matrix, this->w, this->u, this->vt);
    std::cout << "U:" << this->u.size() << std::endl;
    std::cout << "S:" << this->w.size() << std::endl;
    cv::minMaxLoc(this->w, &min , &max);
    std::cout << min << " " << max << std::endl;

}
cv::Mat Channel::compose(double k) {

    cv::Mat sigma, checkValues;

    cv::compare(this->w, k, checkValues, cv::CMP_GT);
    this->w.copyTo(sigma, checkValues);
    sigma = cv::Mat::diag(sigma);
    std::cout << "Rows:\t" << sigma.rows << std::endl;
    std::cout << "k:\t" << k << std::endl;
    return this->u * sigma * this->vt;

}
