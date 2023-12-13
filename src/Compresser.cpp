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
void Compresser::saveImage(std::string p) {

    cv::imwrite(p, this->image);

}
void Compresser::saveChannels(std::string p) {

    cv::FileStorage fs(p, cv::FileStorage::WRITE);
    int i = 0;

    for(Channel j: this->channels) {

        j.save(fs, i);

    }
    fs.release();

}
void Compresser::compose(double k) {

    std::vector<cv::Mat> c;
    cv::Mat compressedImage;

    for(Channel i: this->channels) {

        c.emplace_back(i.compose(k));

    }
    cv::merge(c, compressedImage);
    this->image = compressedImage;

};
