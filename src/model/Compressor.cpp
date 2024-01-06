/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "Compressor.h"

std::vector<std::string> model::Compressor::supportedImageExtensions = {
    // Windows bitmaps
    ".bmp", ".dib",
    //JPEG files
    ".jpeg", ".jpg", ".jpe",
    //JPEG 2000 files
    ".jp2",
    //Portable Network Graphics
    ".png",
    //Portable image format
    ".pbm", ".pgm", ".ppm",
    //Sun rasters
    ".sr", ".ras",
    //TIFF files
    ".tiff", ".tif"
};
std::vector<std::string> model::Compressor::supportedFileExtensions = {
    ".json", ".yaml", ".xml", ".bin"
};

model::Compressor::Compressor(const std::string& file) {

    if(Compressor::isImage(file)) {

        this->loadImage(file);
        return;

    }
    if(Compressor::isFile(file)) {

        this->loadChannels(file);
        return;

    }
    throw new std::invalid_argument("unknown extension for input file");

}
void model::Compressor::loadImage(const std::string& file) {

    cv::Mat image = cv::imread(file, cv::IMREAD_UNCHANGED);
    std::vector<cv::Mat> c;

    image.convertTo(image, CV_64F);
    if(image.empty()) {

        throw new std::invalid_argument("Input file does not exixts");

    }
    cv::split(image, c);
    for(cv::Mat i: c) {

        this->channels.emplace_back(i);

    }

}
void model::Compressor::loadChannels(const std::string& file) {

    int i = 0;
    bool finish = false;
    cv::FileStorage fs(file, cv::FileStorage::READ);

    if(!std::filesystem::exists(std::filesystem::path(file))) {

        throw new std::invalid_argument("Input file does not exixts");

    }
    while(!finish) {

        cv::Mat u, w, vt;
        std::string j = std::to_string(i);

        fs["U_" + j] >> u;
        fs["W_" + j] >> w;
        fs["Vt_" + j] >> vt;
        if(u.empty() || w.empty() || vt.empty()) {

            finish = true;

        } else {

            this->channels.emplace_back(u, w, vt);

        }
        i++;

    }

}

void model::Compressor::saveImage(const std::string& file) {

    std::string extension = std::filesystem::path(file).extension().string();

    std::transform(extension.begin(), extension.end(), extension.begin(), ::tolower);
    this->image.convertTo(this->image, CV_8U);
    if(extension == ".pbm") {

        cv::imwrite(file, this->convertToPbm());
        return;

    }
    if(extension == ".pgm") {

        cv::imwrite(file, this->convertToPgm());
        return;

    }
    cv::imwrite(file, this->image);

}
void model::Compressor::saveChannels(const std::string& file) const {

    cv::FileStorage fs(file, cv::FileStorage::WRITE);
    int i = 0;

    for(Channel j: this->channels) {

        j.save(fs, i);
        i++;

    }
    fs.release();

}
void model::Compressor::compose(double k) {

    std::vector<cv::Mat> c;
    cv::Mat compressedImage;

    for(Channel i: this->channels) {

        c.emplace_back(i.compose(k));

    }
    cv::merge(c, compressedImage);
    this->image = compressedImage;

};
cv::Mat model::Compressor::convertToPgm() const {

    std::vector<cv::Mat> channels;
    cv::Mat result = cv::Mat::zeros(this->image.size(), CV_8UC1);

    cv::split(this->image, channels);
    if(channels.size() >= 3) {

        return 0.114 * channels[0] + 0.587 * channels[1] + 0.299 * channels[2];

    }
    for(cv::Mat i: channels) {

        result += i;

    }
    return result / channels.size();

}
cv::Mat model::Compressor::convertToPbm() const {

    cv::Mat grayscaleImage = this->convertToPgm();

    cv::threshold(grayscaleImage, grayscaleImage, 128, 255, cv::THRESH_BINARY);
    return grayscaleImage;

}
