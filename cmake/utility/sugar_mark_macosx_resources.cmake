# Copyright (c) 2013, Ruslan Baratov
# All rights reserved.

include(sugar_add_this_to_sourcelist)
sugar_add_this_to_sourcelist()

include(sugar_improper_number_of_arguments)

function(sugar_mark_macosx_resources)
  sugar_improper_number_of_arguments(${ARGC} 0)

  set_source_files_properties(
      ${ARGV}
      PROPERTIES
      MACOSX_PACKAGE_LOCATION
      Resources
  )
endfunction()
