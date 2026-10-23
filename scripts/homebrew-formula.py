#!/usr/bin/env python3
"""Render the Homebrew formula for a release from its SHA256SUMS file.

Usage: homebrew-formula.py v0.1.0 dist/SHA256SUMS > Formula/kubrick.rb
"""
import sys

REPO = 'https://github.com/ashark-ai-05/kubrick'
TARGETS = {
    'macos_arm': 'aarch64-apple-darwin',
    'macos_intel': 'x86_64-apple-darwin',
    'linux_arm': 'aarch64-unknown-linux-gnu',
    'linux_intel': 'x86_64-unknown-linux-gnu',
}


def main():
    tag, sums_path = sys.argv[1], sys.argv[2]
    sums = {}
    for line in open(sums_path):
        digest, name = line.split()
        sums[name.lstrip('*')] = digest

    def asset(key):
        name = f'kubrick-{TARGETS[key]}.tar.gz'
        if name not in sums:
            raise SystemExit(f'{name} missing from {sums_path}')
        return f'url "{REPO}/releases/download/{tag}/{name}"\n      sha256 "{sums[name]}"'

    print(f'''class Kubrick < Formula
  desc "Fast, read-only-by-default Kubernetes cluster explorer for the terminal"
  homepage "{REPO}"
  version "{tag.removeprefix('v')}"
  license any_of: ["MIT", "Apache-2.0"]

  on_macos do
    on_arm do
      {asset('macos_arm')}
    end
    on_intel do
      {asset('macos_intel')}
    end
  end

  on_linux do
    on_arm do
      {asset('linux_arm')}
    end
    on_intel do
      {asset('linux_intel')}
    end
  end

  def install
    bin.install "kubrick"
  end

  test do
    assert_match version.to_s, shell_output("#{{bin}}/kubrick --version")
  end
end''')


if __name__ == '__main__':
    main()
