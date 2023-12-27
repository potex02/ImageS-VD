/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "Channel.h"

Channel::Channel(const cv::Mat &matrix) {
	
    cv::SVD svd;

    svd.compute(matrix, this->w, this->u, this->vt);

}
Channel::Channel(const cv::Mat &_u, const cv::Mat &_w, const cv::Mat &_vt): u(_u), w(_w), vt(_vt) {}
void Channel::save(cv::FileStorage &fs, const int i) const {

    std::string j = std::to_string(i);

    fs << "U_" + j << this->u;
    fs << "W_" + j << this->w;
    fs << "Vt_" + j << this->vt;

}
cv::Mat Channel::compose(double k) const {

    cv::Mat sigma, checkValues;

    cv::compare(this->w, k, checkValues, cv::CMP_GT);
    this->w.copyTo(sigma, checkValues);
    sigma = cv::Mat::diag(sigma);
    return this->u * sigma * this->vt;

}
