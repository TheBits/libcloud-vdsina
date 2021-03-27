libcloud драйвер для сервиса vdsina.ru


https://vdsina.ru/tech/api#art-04-05

## Поддерживаемые методы Compute
| Метод | Поддержка |
| --- | --- |
|attach_volume||
|copy_image||
|create_image||
|create_key_pair|-|
|create_node|-|
|create_volume||
|create_volume_snapshot||
|delete_image||
|delete_key_pair|-|
|deploy_node||
|destroy_node|-|
|destroy_volume||
|destroy_volume_snapshot||
|detach_volume||
|features||
|get_image||
|get_key_pair|-|
|import_key_pair_from_file|-|
|import_key_pair_from_string|-|
|list_images|-|
|list_key_pairs|-|
|list_locations|-|
|list_nodes|-|
|list_sizes|-|
|list_volume_snapshots||
|list_volumes||
|reboot_node|-|
|start_node||
|stop_node||
|wait_until_running||




## Методы DNS
| Метод | Поддержка |
| --- | --- |
|list zones||
|list records||
|create zone||
|update zone||
|create record||
|update record||
|delete zone||
|delete record||


## Разработка

В проекте настроена автоматическая проверка линтерами и тестами.

Линтеры запускаются в `pre-commit`, тесты в `pytest`.
