# RecSys Challenge: Book Recommendation

## Introduction

The repository keeps trace of the working procedure of the recommender system challenge on Kaggle (https://www.kaggle.com/competitions/recommender-system-2023-challenge-polimi).

The problem consists in generating potentially relevant book recommendations for users, given a dataset of user-item interactions. 

## Repository Structure

- [**Input/**](Input) contains the original data ([data_train.csv](data_train.csv) and [data_target_users_test.csv](data_target_users_test.csv)),
along with saved k-fold splitting and separate train-validation sets.

- [**Workspace/**](Workspace) is cloned from the course repository [**RecSys_Course_AT_PoliMi**](https://github.com/MaurizioFD/RecSys_Course_AT_PoliMi) with some minor modifications of the code.
It contains the implementations of various recommender algorithms and utility functions. 

- [**Notebooks/**](Notebooks) contains part of personal notebook files used for the challenge.
