printf "Creating dirs\n";
mkdir packages config;


printf "1. Downloading wp-cli.phar\n";
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar;


printf "\n...\n";
php wp-cli.phar --info;


printf "\n...\n";
printf "2. Move wp-cli.phar --> /usr/local/bin/wp\n";
chmod +x wp-cli.phar;
sudo mv wp-cli.phar /usr/local/bin/wp;
sudo wp cli update;


printf "\n...\n";
wp --info;
printf "\n...\n";


printf "3. Install Tab Completions\n";
printf "SRC: https://github.com/wp-cli/wp-cli\n";
curl -O https://raw.githubusercontent.com/wp-cli/wp-cli/v1.5.1/utils/wp-completion.bash;


echo "

# autoload bashcompinit
# bashcompinit
source $PWD/wp-completion.bash

" >> $HOME/.bashrc;


source $HOME/.bashrc;
