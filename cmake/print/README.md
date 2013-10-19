Wrappers for `message` command to control output:
 * `sugar_status_print` - prints only if [SUGAR_STATUS_PRINT](https://github.com/ruslo/sugar/wiki/Used-variables) is setted to `TRUE`
 * `sugar_status_debug` - prints only if [SUGAR_STATUS_DEBUG](https://github.com/ruslo/sugar/wiki/Used-variables) is setted to `TRUE`
 * `sugar_fatal_error` - wrapper for `message(FATAL_ERROR "...")`
