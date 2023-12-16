#include "Compresser.h"

std::vector<std::string> Compresser::supportedExtensions = {
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
    ".sr", ".ras"
    //TIFF files
    ".tiff", ".tif"
};

Compresser::Compresser(const std::string &file) {

    if(Compresser::isImage(file)) {

        this->loadImage(file);

    } else {

        this->loadChannels(file);

    }

}
inline bool Compresser::isImage(const std::string &file) {

    std::filesystem::path p(file);

    return std::find(Compresser::supportedExtensions.begin(), Compresser::supportedExtensions.end(), p.extension()) != Compresser::supportedExtensions.end();

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

    int i = 0;
    bool finish = false;
    cv::FileStorage fs(file, cv::FileStorage::READ);

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
    cv::Mat result = cv::Mat::zeros(this->image.size(), CV_64FC1);

    cv::split(this->image, channels);
    for(cv::Mat i: channels) {

        result += i;

    }
    return result / channels.size();

}
