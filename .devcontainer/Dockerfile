FROM rdocker.ptin.corppt.com/extsw-base-ub/ub20:latest

ENV DEBIAN_FRONTEND=noninteractive \
	TZ=Europe/Lisbon

ARG USER=vscode
ARG GROUP=vscode
ARG UUID=1000
ARG GUID=1000

# Set timezone (needed for tzdata package)
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install packages
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y --no-install-recommends sudo locales ca-certificates zsh git openssh-client ansible ansible-lint python3-jmespath gnupg2 && \
	rm -rf /var/lib/apt/lists/* && \
	localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF- && \
	wget -c http://ca.ptin.corppt.com/alticelabs-ca.crt -P /usr/local/share/ca-certificates/ && update-ca-certificates

# Setup user
RUN groupadd -r -g ${GUID} ${GROUP} && \
	useradd --no-log-init -r -u ${UUID} -g ${GUID} -m ${USER} && \
	usermod -a -G sudo ${USER} && \
	echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Setup shell
USER ${USER}

RUN mkdir /home/${USER}/.ssh

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.2/zsh-in-docker.sh)" -- \
		-t robbyrussell \
		echo "PROMPT='%B%F{cyan}%1~%f %F{178}$%f %b'" >> /home/${USER}/.zshrc

#WORKDIR /home/${USER}/src
