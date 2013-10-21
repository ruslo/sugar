# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

if(DEFINED RESOURCES_IOS_IMAGES_SUGAR_CMAKE)
  return()
else()
  set(RESOURCES_IOS_IMAGES_SUGAR_CMAKE 1)
endif()

include(sugar_files)

sugar_files(
    DEFAULT_IOS_IMAGES
    Default-568h@2x.png
    Default.png
    Default@2x.png
)
