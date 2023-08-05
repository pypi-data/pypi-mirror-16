/*
 * Copyright 2015 FUJITSU LIMITED
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */

package monasca.log.api.common;

import javax.annotation.Nullable;
import javax.ws.rs.core.MediaType;

import com.google.common.base.Function;

import monasca.log.api.model.Log;

abstract public class PayloadTransformer
    implements Function<String, Log> {

  public abstract Log transform(final String from);

  public abstract MediaType supportsMediaType();

  @Nullable
  @Override
  public final Log apply(@Nullable final String input) {
    return this.transform(input);
  }

}
