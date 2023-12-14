#include "Compresser.h"

Compresser::Compresser(const std::string &file) {

    std::filesystem::path p(file);

    if(p.extension() == ".png" || p.extension() == ".jpg" || p.extension() == ".jpeg") {

        this->loadImage(file);

    } else {

        this->loadChannels(file);

    }

}
void Compresser::loadImage(const std::string &file) {

    cv::Mat image = cv::imread(file);
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
void Compresser::loadChannels(const std::string &file) {

    cv::FileStorage fs(file, cv::FileStorage::READ);

}

void Compresser::saveImage(const std::string &file) {

    cv::imwrite(file, this->image);

}
void Compresser::saveChannels(const std::string &file) {

    cv::FileStorage fs(file, cv::FileStorage::WRITE);
    int i = 0;

    for(Channel j: this->channels) {

        j.save(fs, i);
        i++;

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
