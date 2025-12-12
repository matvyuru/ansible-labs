#!/bin/bash
echo "=== Запуск управляемого узла ==="

# Проверяем установлен ли Docker
if ! command -v docker &> /dev/null; then
    echo "Docker не установлен. Установка..."
    sudo apt update
    sudo apt install -y docker.io docker-compose
    sudo usermod -aG docker $USER
    echo "Перезайдите в систему или выполните: newgrp docker"
    exit 1
fi

echo "1. Запускаем контейнер..."
docker-compose up -d

echo "2. Ждем запуск SSH..."
sleep 10

echo "3. Проверяем состояние..."
docker ps | grep ansible-managed-node

echo ""
echo "=== Управляемый узел готов ==="
echo "SSH подключение:"
echo "  ssh root@localhost -p 2222"
echo "  Пароль: ansible123"
echo ""
echo "Ansible inventory уже настроен в inventory/hosts.ini"
