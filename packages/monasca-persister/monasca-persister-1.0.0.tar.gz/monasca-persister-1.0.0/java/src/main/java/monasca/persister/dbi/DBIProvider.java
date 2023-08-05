/*
 * Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package monasca.persister.dbi;

import monasca.persister.configuration.PersisterConfig;

import com.google.inject.ProvisionException;

import io.dropwizard.jdbi.DBIFactory;
import io.dropwizard.setup.Environment;

import org.skife.jdbi.v2.DBI;

import javax.inject.Inject;
import javax.inject.Provider;

public class DBIProvider implements Provider<DBI> {

  private final Environment environment;
  private final PersisterConfig configuration;

  @Inject
  public DBIProvider(Environment environment, PersisterConfig configuration) {
    this.environment = environment;
    this.configuration = configuration;
  }

  @Override
  public DBI get() {
    try {
      return new DBIFactory().build(environment, configuration.getDataSourceFactory(), "vertica");
    } catch (ClassNotFoundException e) {
      throw new ProvisionException("Failed to provision DBI", e);
    }
  }
}
