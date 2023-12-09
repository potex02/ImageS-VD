#include "channel.h"

Channel::Channel(cv::Mat matrix) {

    double min, max;
    cv::SVD svd;

    svd.compute(matrix, this->w, this->u, this->vt);
    cv::minMaxLoc(this->w, &min , &max);
    std::cout << min << " " << max << std::endl;

}
void Channel::save(cv::FileStorage &fs, int i) {

    fs << "U_" + i << this->u;
    fs << "W_" + i << this->w;
    fs << "Vt_" + i << this->vt;

}
cv::Mat Channel::compose(double k) {

    cv::Mat sigma, checkValues;

    cv::compare(this->w, k, checkValues, cv::CMP_GT);
    this->w.copyTo(sigma, checkValues);
    sigma = cv::Mat::diag(sigma);
    return this->u * sigma * this->vt;

}
