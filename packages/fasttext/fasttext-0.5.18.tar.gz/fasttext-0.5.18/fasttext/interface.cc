/* An interface for fastText */
#include <iostream>
#include <string>
#include <vector>

#include "interface.h"
#include "cpp/src/real.h"
#include "cpp/src/args.h"
#include "cpp/src/dictionary.h"
#include "cpp/src/matrix.h"
#include "cpp/src/vector.h"

#include "cpp/src/fasttext.cc"

FastTextModel::FastTextModel(){}

std::vector<std::string> FastTextModel::getWords()
{
    return _words;
}

Dictionary FastTextModel::getDictionary()
{
    return _dict;
}

void FastTextModel::addWord(std::string word)
{
    _words.push_back(word);
}

void FastTextModel::setDict(Dictionary dict)
{
    _dict = dict;
}

void FastTextModel::setMatrix(Matrix matrix)
{
    _matrix = matrix;
}

void FastTextModel::setArg(Args arg)
{
    dim = arg.dim;
    ws = arg.ws;
    epoch = arg.epoch;
    minCount = arg.minCount;
    neg = arg.neg;
    wordNgrams = arg.wordNgrams;
    if(arg.loss == loss_name::ns) {
        lossName = "ns";
    }
    if(arg.loss == loss_name::hs) {
        lossName = "hs";
    }
    if(arg.loss == loss_name::softmax) {
        lossName = "softmax";
    }
    if(arg.model == model_name::cbow) {
        modelName = "cbow";
    }
    if(arg.model == model_name::sg) {
        modelName = "skipgram";
    }
    if(arg.model == model_name::sup) {
        modelName = "supervised";
    }
    bucket = arg.bucket;
    minn = arg.minn;
    maxn = arg.maxn;
    lrUpdateRate = arg.lrUpdateRate;
    t = arg.t;
}

std::vector<real> FastTextModel::getVectorWrapper(std::string word)
{
    Vector vec(dim);
    getVector(_dict, _matrix, vec, word);
    std::vector<real> vector(vec.data_, vec.data_ + vec.m_);
    return vector;
}

void trainWrapper(int argc, char **argv, int silent)
{
    /* output file stream to redirect output from fastText library */
    std::string temp_file_name = std::tmpnam(nullptr);
    std::ofstream new_ofs(temp_file_name);
    std::streambuf* old_ofs = std::cout.rdbuf();

    /* if silent > 0, the log from train() function will be supressed */
    if(silent > 0) {
        std::cout.rdbuf(new_ofs.rdbuf());
        train(argc, argv);
        std::cout.rdbuf(old_ofs);
    } else {
        train(argc, argv);
    }

    new_ofs.close();
}

void loadModelWrapper(std::string filename, FastTextModel& model)
{
    Dictionary dict;
    Matrix input, output;
    loadModel(filename, dict, input, output);

    /* args is defined globally in cpp/src/fasttext.cc
     * We parse it to the model, so we not depend on it anymore */
    model.setArg(args);
    model.setDict(dict);
    model.setMatrix(input);

    /* Do the indexing on Cython instead to support unicode
     * instead of plain bytes */
    /*
    for(int32_t i = 0; i < dict.nwords(); i++) {
        std::string word  = dict.getWord(i);
        model.addWord(word);
    }
    */
}
