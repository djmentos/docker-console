from docker_console.web.engines.base.commands import commands

drupal_commands = {
    'build': [
        'confirm_action',
        'docker.docker_run("docker-console build-in-docker")',
        'docker.chown',
        'docker.setfacl',
        'chmod_files'
    ],
    'up-and-build': [
        'confirm_action',
        'docker.docker_up',
        'docker.docker_run("docker-console build-in-docker")',
        'docker.chown',
        'docker.setfacl',
        'chmod_files'
    ],
    'build-in-docker': [
        'drupal_settings.copy_settings("drupal8")',
        'database.drop_db',
        'database.create_db',
        'database.import_db',
        'drush.en("devel")',
        'drush.run("cc all")',
        'drush.run("uli")'
    ],
    'drush': [
        'docker.drush_run'
    ],
}

commands.update(drupal_commands)
