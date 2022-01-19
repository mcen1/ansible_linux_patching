logstash {
  ansiColor('xterm') {
    node (label: 'patching') {

      stage ("Checkout scm") {
        checkout scm
        currentBuild.displayName = "${ANSSERVERS}"
        currentBuild.description = "Patching is underway."
      }
      stage ("Decrypt ssh keys") {
        withCredentials([file(credentialsId: "ansible_vault", variable: 'ANSVAULT')]) {
          sh "ansible-vault decrypt ansible_resources/supporting_tools/id_rsa --vault-password-file='${ANSVAULT}'"
        }
      }
      stage ("Patching servers") {
        // This is a custom function we've written. It tends to boil down to "ansible-playbook -u sa-ansible '--private-key=****' -e playbook_strategy=free -i ansible_resources/inventories/dynamic_inventory_from_env.py -l ' server1 server2 server3 [...] server60' ansible_resources/playbooks/patch_automation.yml '--vault-password-file=****'"
        PatchingPlaybook(ANSEXTRASWITCHES: "${ANSEXTRASWITCHES}", ANSSERVERS: "${ANSSERVERS}", PLAYBOOK: "${PLAYBOOK}", ANSINV: "${ANSINV}", ANSCLIVARS: "${ANSCLIVARS}")
      }
    }
  }
}

