#include "Compresser.h"

std::vector<std::string> Compresser::supportedImageExtensions = {
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
std::vector<std::string> Compresser::supportedFileExtensions = {
    ".json", ".yaml", ".xml", ".bin"
};

Compresser::Compresser(const std::string &file) {

    if(Compresser::isImage(file)) {

        this->loadImage(file);
        return;

    }
    if(Compresser::isFile(file)) {

        this->loadChannels(file);
        return;

    }
    throw new std::invalid_argument("unknown extension for input file");

}
bool Compresser::isImage(const std::string &file) {

    std::filesystem::path p(file);

    return std::find(Compresser::supportedImageExtensions.begin(), Compresser::supportedImageExtensions.end(), p.extension()) != Compresser::supportedImageExtensions.end();

}
bool Compresser::isFile(const std::string &file) {

    std::filesystem::path p(file);

    return std::find(Compresser::supportedFileExtensions.begin(), Compresser::supportedFileExtensions.end(), p.extension()) != Compresser::supportedFileExtensions.end();

}
void Compresser::loadImage(const std::string &file) {

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
void Compresser::loadChannels(const std::string &file) {

    int i = 0;
    bool finish = false;
    cv::FileStorage fs(file, cv::FileStorage::READ);

    if(!std::filesystem::exists(std::filesystem::path(file))) {

        throw new std::invalid_argument("Input file does not exixts");

    }
    while(!finish) {

        cv::Mat u, w, vt;

        fs["U_" + std::to_string(i)] >> u;
        fs["W_" + std::to_string(i)] >> w;
        fs["Vt_" + std::to_string(i)] >> vt;
        if(u.empty() || w.empty() || vt.empty()) {

            finish = true;

        } else {

            this->channels.emplace_back(u, w, vt);

        }
        i++;

    }

}

void Compresser::saveImage(const std::string &file) {

    std::filesystem::path p(file);

    this->image.convertTo(this->image, CV_8U);
    if(p.extension() == ".pbm") {

        cv::imwrite(file, this->convertToPbm());
        return;

    }
    if(p.extension() == ".pgm") {

        cv::imwrite(file, this->convertToPgm());
        return;

    }
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
cv::Mat Compresser::convertToPgm() {

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
cv::Mat Compresser::convertToPbm() {

    cv::Mat grayscaleImage = this->convertToPgm();

    cv::threshold(grayscaleImage, grayscaleImage, 128, 255, cv::THRESH_BINARY);
    return grayscaleImage;

}
