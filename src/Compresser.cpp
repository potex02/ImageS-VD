#include "Compresser.h"

Compresser::Compresser(std:: string path) {

    cv::Mat image = cv::imread(path);
    std::vector<cv::Mat> c;

    image.convertTo(image, CV_64F);
    if(image.empty()) {

        throw new std::exception();

    }
    cv::split(image, c);
    for(cv::Mat i: c) {

        this->channels.emplace_back(i);

    }

}
void Compresser::save() {

    cv::FileStorage fs("output.json", cv::FileStorage::WRITE);
    int i = 0;

    for(Channel j: this->channels) {

        j.save(fs, i);

    }
    fs.release();

}
cv::Mat Compresser::compose(double k) {

    std::vector<cv::Mat> c;
    cv::Mat compressedImage;

    for(Channel i: this->channels) {

        c.emplace_back(i.compose(k));

    }
    cv::merge(c, compressedImage);
    return compressedImage;

};
