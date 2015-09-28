#!/usr/bin/python

import sys, os
sys.path.append('docker-dev-env')

import dockerenv


def main():
    cache_fname = os.path.join(os.path.dirname(__file__), 'docker_image_cache.json')
    with dockerenv.stored_cache(cache_fname) as cache:
        return dockerenv.main(
            env = dockerenv.DockerEnv(
                base_dir = os.path.abspath(os.path.dirname(__file__)),
                base_image = 'python:3.5.0-slim',
                builders = dockerenv.get_wrapped_script_builders('setup', 'brewery/setup'),
                image_cache = cache,
            ),
        )


if __name__ == '__main__':
    main()

