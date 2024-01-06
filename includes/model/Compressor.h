/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#pragma once
#include <stdexcept>
#include <vector>
#include <algorithm>
#include <filesystem>
#include <opencv2/opencv.hpp>
#include "Channel.h"

/**
 * Contains classes related to the application's model following the MVC architecture.
 *
 * Classes:
 *   - @ref model::Compressor: Implementation of a image compressor through the SVD decomposition.
 *   - @ref model::Channel: Representation of a SVD decomposition of a matrix.
 */
namespace model {

    /**
     * Implementation of a image compressor through the SVD decomposition.
     *
     * The class splits the channels of an image and permits to decompose them.
     * It also permits to save the channels or, starting from them, to recompose the image and save it.
     * It uses, to work with channels, the Channel class.
     */
    class Compressor {

        public:
            /**
             * The vector of the supported image extensions from the app.
             */
            static std::vector<std::string> supportedImageExtensions;
            /**
             * The vector of the supported file extensions to save the channels from the app.
             */
            static std::vector<std::string> supportedFileExtensions;
            /**
             * Create a Compressor from the file.
             *
             * If the file is a supported image, it reads and decomposes the image.
             * If the file is a data file, it loads the channels from it.
             *
             * @param file is the file from which to read the data.
             * @throw an std::invalid_argument is the file has an unsupported exception.
             */
            Compressor(const std::string& file);
            /**
             * Check if the input file is a supported image or file to save the channels.
             *
             * @param file is the path of the file to be checked.
             * @return true if the file is a supported file.
             */
            static inline bool isValid(const std::string& file) {

                return Compressor::isImage(file) || Compressor::isFile(file);

            }
            /**
             * Check if the input file is a supported image.
             *
             * @param file is the path of the file to be checked.
             * @return true if the file is a supported image.
             */
            static inline bool isImage(const std::string& file) {

                std::string extension = std::filesystem::path(file).extension().string();

                std::transform(extension.begin(), extension.end(), extension.begin(), ::tolower);
                return std::find(Compressor::supportedImageExtensions.begin(), Compressor::supportedImageExtensions.end(), extension) != Compressor::supportedImageExtensions.end();

            }
            /**
             * Check if the input file is a supported file to save the channels.
             *
             * @param file is the path of the file to be checked.
             * @return true if the file is a supported file.
             */
            static inline bool isFile(const std::string& file) {

                std::string extension = std::filesystem::path(file).extension().string();

                std::transform(extension.begin(), extension.end(), extension.begin(), ::tolower);
                return std::find(Compressor::supportedFileExtensions.begin(), Compressor::supportedFileExtensions.end(), extension) != Compressor::supportedFileExtensions.end();

            }
            /**
             * Load an image from a file.
             *
             * @param file is the path of the image.
             * @throw an std::invalid_argument if the file does not exist.
             */
            void loadImage(const std::string& file);
            /**
             * Load and create the channels from the file.
             *
             * @param file is the path of the file.
             * @throw an std::invalid_argument if the file does not exist.
             */
            void loadChannels(const std::string& file);
            /**
             * Save the image.
             *
             * @param file is the path where to save the image,
             */
            void saveImage(const std::string& file);
            /**
             * Save the channels.
             *
             * @param file is the path where to save the channels.
             */
            void saveChannels(const std::string& file) const;
            /**
             * Compose and merge the channels.
             *
             * @param k is the threshold of the singular values.
             */
            void compose(double k);
        private:
            /**
             * The image resulting from the compression.
             */
            cv::Mat image;
            /**
             * the vector of decomposed channels of the image.
             */
            std::vector<Channel> channels;
            /**
             * Convert the image to grayscale for saving it in .pgm format.
             *
             * @return the grayscale image.
             */
            cv::Mat convertToPgm() const;
            /**
             * Convert the image to black and white for saving it in .pbm format.
             *
             * @return the black and white image.
             */
            cv::Mat convertToPbm() const;

    };

}
