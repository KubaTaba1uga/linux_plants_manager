READ_SENSORS_JOB_VERSION = 1.0
READ_SENSORS_JOB_SOURCE = read_sensors_job.py
READ_SENSORS_JOB_SITE_METHOD = local
READ_SENSORS_JOB_SITE = ../read_sensors_job
READ_SENSORS_JOB_INSTALL_TARGET = usr/bin
READ_SENSORS_JOB_DEPENDENCIES = python3

define READ_SENSORS_JOB_INSTALL_TARGET_CMDS
	$(INSTALL) -D -m 0755 $(@D)/read_sensors_job.py \
		$(TARGET_DIR)/usr/bin/read_sensors_job.py
endef

$(eval $(generic-package))

# * * * * * python3 /usr/bin/read_sensors_job.py
