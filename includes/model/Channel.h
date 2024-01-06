/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#pragma once
#include <opencv2/opencv.hpp>

namespace model {

    /**
     * Representation of a SVD decomposition of a matrix.
     */
    class Channel {

        public:
            /**
             * Create Channel decomposing the matrix parameter using the SVD decomposition.
             *
             * @param matrix is the matrix which is decomposed in the u, w (or sigma) and vt matrices
             */
            Channel(const cv::Mat& matrix);
            /**
             * Create Channel with the specified parameters.
             *
             * @param _u is the u matrix.
             * @param _w is the w (or sigma) matrix.
             * @param _vt is the transposed v matrix.
             */
            Channel(const cv::Mat& _u, const cv::Mat& _w, const cv::Mat& _vt);
            /**
             * Save the u, w (or sigma) and vt matrices on the file system.
             *
             * @param fs is the cv::FileStorage used to save the Channel.
             * @param i is the number of the current Channel in the matrix.
             */
            void save(cv::FileStorage& fs, const int i) const;
            /**
             * Compose the matrix from u, w (or sigma) and vt.
             *
             * @param k is the threshold of the singular values.
             * @return the composed matrix.
             */
            cv::Mat compose(double k) const;
        private:
            /**
             * The u matrix of the SVD decomposition of the matrix.
             */
            cv::Mat u;
            /**
             * The w matrix of the SVD decomposition of the matrix, also referred as sigma.
             */
            cv::Mat w;
            /**
             * The transposed v matrix of the SVD decomposition of the matrix.
             */
            cv::Mat vt;

    };

}
