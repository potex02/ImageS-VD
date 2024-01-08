/*
 * This file is part of ImageS-VD Application.
 * See the file LICENSE for licensing information.
 */
#include "Action.h"

control::Action::Action(std::function<void ()> _fun): fun(_fun) {}
