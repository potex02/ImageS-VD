#include "channel.h"

Channel::Channel(const cv::Mat &matrix) {

    double min, max;
    cv::SVD svd;

    svd.compute(matrix, this->w, this->u, this->vt);
    cv::minMaxLoc(this->w, &min , &max);
    std::cout << min << " " << max << std::endl;

}
Channel::Channel(const cv::Mat &_u, const cv::Mat &_w, const cv::Mat &_vt): u(_u), w(_w), vt(_vt) {}
void Channel::save(cv::FileStorage &fs, int i) {

    fs << "U_" + std::to_string(i) << this->u;
    fs << "W_" + std::to_string(i) << this->w;
    fs << "Vt_" + std::to_string(i) << this->vt;

}
cv::Mat Channel::compose(double k) {

    cv::Mat sigma, checkValues;

    cv::compare(this->w, k, checkValues, cv::CMP_GT);
    this->w.copyTo(sigma, checkValues);
    sigma = cv::Mat::diag(sigma);
    return this->u * sigma * this->vt;

}
